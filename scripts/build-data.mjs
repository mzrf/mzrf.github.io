#!/usr/bin/env node
/**
 * 抓取基金历史净值，计算涨跌幅、区间表现、历史分位与估值星级，输出 data/funds.js 与 data/funds.json。
 * 数据源：天天基金 pingzhongdata（单请求返回建仓以来全量单位净值）
 * 用法：node scripts/build-data.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SOURCE_HOST = 'https://fund.eastmoney.com';
const UA = 'Mozilla/5.0 (compatible; FundDashboard/1.0)';

/* ---------- 工具 ---------- */
const round = (v, n = 4) => (v == null || !Number.isFinite(v) ? null : Number(v.toFixed(n)));
const pct = (v, n = 2) => (v == null || !Number.isFinite(v) ? null : Number(v.toFixed(n)));

/** 从 pingzhongdata 脚本里截取 var NAME = <字面量>; 的原文 */
function grabLiteral(src, name) {
  const key = `var ${name}`;
  let i = src.indexOf(key);
  if (i < 0) return null;
  let k = src.indexOf('=', i + key.length) + 1;
  while (k < src.length && /\s/.test(src[k])) k++;
  const open = src[k];
  if (open === '"') {
    const end = src.indexOf('"', k + 1);
    return src.slice(k, end + 1);
  }
  if (open !== '[' && open !== '{') return null;
  const close = open === '[' ? ']' : '}';
  let depth = 0, inStr = false, esc = false;
  for (let t = k; t < src.length; t++) {
    const c = src[t];
    if (inStr) {
      if (esc) esc = false;
      else if (c === '\\') esc = true;
      else if (c === '"') inStr = false;
      continue;
    }
    if (c === '"') { inStr = true; continue; }
    if (c === open) depth++;
    else if (c === close) {
      depth--;
      if (depth === 0) return src.slice(k, t + 1);
    }
  }
  return null;
}

function grabValue(src, name) {
  const lit = grabLiteral(src, name);
  if (lit == null) return null;
  if (lit.startsWith('"')) return lit.slice(1, -1);
  try { return JSON.parse(lit); } catch { return null; }
}

/** 接口时间戳是北京时间当日 00:00（即前一日 16:00 UTC），按 UTC+8 取值才拿到正确的日期 */
const fmtDate = (ms) => new Date(ms + 8 * 3600 * 1000).toISOString().slice(0, 10);

/* ---------- 计算 ---------- */
const isLeap = (y) => (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;
const daysOfYear = (y) => (isLeap(y) ? 366 : 365);

/** 从序列末尾往前找日期 <= 目标日的最后一条（交易日近似） */
function navAtOrBefore(series, targetDate) {
  let lo = 0, hi = series.length - 1, ans = -1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (series[mid].date <= targetDate) { ans = mid; lo = mid + 1; }
    else hi = mid - 1;
  }
  return ans >= 0 ? series[ans] : null;
}

/** 按交易日偏移取区间涨跌幅 */
function byTradingDays(series, latest, n) {
  const idx = series.length - 1 - n;
  if (idx < 0) return null;
  return pct((latest.nav / series[idx].nav - 1) * 100);
}

/** 按自然年数回溯取区间涨跌幅（不够长返回 null） */
function byYears(series, latest, years) {
  const target = new Date(latest.date);
  target.setUTCFullYear(target.getUTCFullYear() - years);
  const from = navAtOrBefore(series, target.toISOString().slice(0, 10));
  if (!from) return null;
  return pct((latest.nav / from.nav - 1) * 100);
}

/** 当前值在窗口内的历史分位（0 = 历史最低，100 = 历史最高） */
function percentileOf(values, current) {
  if (!values.length) return null;
  let below = 0;
  for (const v of values) if (v < current) below++;
  let equal = 0;
  for (const v of values) if (v === current) equal++;
  return pct(((below + equal * 0.5) / values.length) * 100, 1);
}

/** 净值分位 → 估值星级：分位越低，相对历史越便宜，星级越高 */
function starsFromPercentile(p) {
  if (p == null) return null;
  if (p <= 20) return 5;
  if (p <= 40) return 4;
  if (p <= 60) return 3;
  if (p <= 80) return 2;
  return 1;
}

/** 年化收益（按自然日折算） */
function annualized(totalReturn, days) {
  if (totalReturn == null || days <= 0) return null;
  const years = days / 365.25;
  if (years < 0.08) return null;
  const base = 1 + totalReturn / 100;
  if (base <= 0) return null;
  return pct((Math.pow(base, 1 / years) - 1) * 100);
}

/** 最大回撤（窗口内） */
function maxDrawdown(series) {
  let peak = -Infinity, dd = 0, peakDate = null, troughDate = null, bestPeak = null, bestTrough = null;
  for (const p of series) {
    if (p.nav > peak) { peak = p.nav; peakDate = p.date; }
    const cur = (p.nav / peak - 1) * 100;
    if (cur < dd) { dd = cur; bestPeak = peakDate; bestTrough = p.date; }
  }
  return { pct: pct(dd), from: bestPeak, to: bestTrough };
}

/** 年化波动率（日收益标准差 × √244） */
function volatility(series) {
  if (series.length < 30) return null;
  const rets = [];
  for (let i = 1; i < series.length; i++) {
    if (series[i - 1].nav > 0) rets.push(series[i].nav / series[i - 1].nav - 1);
  }
  const mean = rets.reduce((a, b) => a + b, 0) / rets.length;
  const sq = rets.reduce((a, b) => a + (b - mean) ** 2, 0) / (rets.length - 1);
  return pct(Math.sqrt(sq) * Math.sqrt(244) * 100);
}

/** XIRR：现金流不定期的内部收益率（二分法，年化） */
function xirr(flows) {
  const t0 = flows[0].date;
  const npv = (r) => flows.reduce((sum, f) => {
    const years = (new Date(f.date) - new Date(t0)) / (365.25 * 24 * 3600 * 1000);
    return sum + f.amount / Math.pow(1 + r, years);
  }, 0);
  let lo = -0.9999, hi = 5;
  if (npv(lo) * npv(hi) > 0) return null;
  for (let i = 0; i < 200; i++) {
    const mid = (lo + hi) / 2;
    const v = npv(mid);
    if (Math.abs(v) < 1e-7) return pct(mid * 100);
    if (npv(lo) * v <= 0) hi = mid; else lo = mid;
  }
  return pct(((lo + hi) / 2) * 100);
}

/** 周定投回测：每周一投入 amount 元，按当日（或最近交易日）净值买入，不计申赎费用 */
function dcaBacktest(series, amount, years = 5) {
  const first = series[0].date;
  const last = series[series.length - 1];
  const t = new Date(last.date);
  t.setUTCFullYear(t.getUTCFullYear() - years);
  const startDate = t.toISOString().slice(0, 10) > first ? t.toISOString().slice(0, 10) : first;

  const flows = [];
  let cursor = new Date(startDate + 'T00:00:00Z');
  cursor.setUTCDate(cursor.getUTCDate() + ((8 - cursor.getUTCDay()) % 7)); // 下一个周一
  let shares = 0, invested = 0, count = 0;
  while (true) {
    const d = cursor.toISOString().slice(0, 10);
    if (d > last.date) break;
    const row = navAtOrBefore(series, d);
    if (row && row.date >= startDate) {
      shares += amount / row.nav;
      invested += amount;
      count++;
      flows.push({ date: row.date, amount: -amount });
    }
    cursor = new Date(cursor.getTime() + 7 * 24 * 3600 * 1000);
  }
  if (!count) return { amount, years, weeks: 0, invested: 0, shares: 0, value: 0, profit: 0, profitRate: null, irr: null };
  const value = shares * last.nav;
  flows.push({ date: last.date, amount: value });
  return {
    amount,
    years,
    weeks: count,
    startDate,
    invested: round(invested, 2),
    shares: round(shares, 4),
    value: round(value, 2),
    profit: round(value - invested, 2),
    profitRate: pct((value / invested - 1) * 100),
    irr: xirr(flows),
  };
}

/** 年度收益表（首尾年按区间收益，其余按自然年） */
function yearlyReturns(series) {
  const byYear = new Map();
  for (const p of series) {
    const y = p.date.slice(0, 4);
    if (!byYear.has(y)) byYear.set(y, { start: p.nav, end: p.nav, first: p.date, last: p.date });
    const o = byYear.get(y);
    o.end = p.nav; o.last = p.date;
  }
  const out = [];
  let prevClose = null;
  for (const [y, o] of byYear) {
    const base = prevClose ?? o.start;
    out.push({ year: y, ret: pct((o.end / base - 1) * 100), partial: false });
    prevClose = o.end;
  }
  if (out.length) {
    // 标记首末年为不完整年度
    out[0].partial = true;
    out[out.length - 1].partial = series[series.length - 1].date.slice(5) !== '12-31';
  }
  return out;
}

/** 向下采样，保留首尾与极值点 */
function downsample(series, maxPoints = 900) {
  if (series.length <= maxPoints) return series;
  const step = Math.ceil(series.length / maxPoints);
  const out = [];
  for (let i = 0; i < series.length; i += step) out.push(series[i]);
  if (out[out.length - 1] !== series[series.length - 1]) out.push(series[series.length - 1]);
  return out;
}

/* ---------- 抓取 ---------- */
async function fetchScript(code, attempt = 1) {
  const url = `${SOURCE_HOST}/pingzhongdata/${code}.js`;
  const res = await fetch(url, {
    headers: { 'User-Agent': UA, Referer: `${SOURCE_HOST}/` },
    signal: AbortSignal.timeout(20000),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const text = await res.text();
  if (!text.includes('Data_netWorthTrend')) throw new Error('返回内容不含净值序列');
  return text;
}

async function buildFund(entry) {
  const code = String(entry.code ?? entry).trim();
  if (!/^\d{6}$/.test(code)) throw new Error(`基金代码不合法：${code}`);

  let src;
  for (let i = 1; i <= 3; i++) {
    try { src = await fetchScript(code, i); break; } catch (e) {
      if (i === 3) throw new Error(`${code} 抓取失败：${e.message}`);
      await new Promise(r => setTimeout(r, 1200 * i));
    }
  }

  const name = grabValue(src, 'fS_name') || code;
  const rawTrend = grabValue(src, 'Data_netWorthTrend') || [];
  const rawAcc = grabValue(src, 'Data_ACWorthTrend') || [];
  const series = rawTrend
    .filter(p => Number.isFinite(p.y) && p.y > 0)
    .map(p => ({ date: fmtDate(p.x), nav: p.y, chg: p.equityReturn == null ? null : Number(p.equityReturn) }));
  if (series.length < 2) throw new Error(`${code} 净值序列过短`);

  const accMap = new Map(rawAcc.map(a => [fmtDate(a[0]), a[1]]));
  const latest = series[series.length - 1];
  const prev = series[series.length - 2];
  const first = series[0];

  const nav5yStart = (() => {
    const t = new Date(latest.date); t.setUTCFullYear(t.getUTCFullYear() - 5);
    return t.toISOString().slice(0, 10);
  })();
  const win5y = series.filter(p => p.date >= nav5yStart);
  const win3y = series.filter(p => { const t = new Date(latest.date); t.setUTCFullYear(t.getUTCFullYear() - 3); return p.date >= t.toISOString().slice(0, 10); });

  const pct5y = percentileOf(win5y.map(p => p.nav), latest.nav);
  const pct3y = percentileOf(win3y.map(p => p.nav), latest.nav);
  const pctAll = percentileOf(series.map(p => p.nav), latest.nav);
  const starBasis = win5y.length > 250 ? pct5y : pctAll;

  const win5yLow = win5y.reduce((a, b) => (b.nav < a.nav ? b : a), win5y[0]);
  const win5yHigh = win5y.reduce((a, b) => (b.nav > a.nav ? b : a), win5y[0]);

  const ytdBase = (() => {
    const firstThisYear = series.find(p => p.date >= `${latest.date.slice(0, 4)}-01-01`);
    if (!firstThisYear) return null;
    const idx = series.indexOf(firstThisYear);
    return idx > 0 ? series[idx - 1].nav : firstThisYear.nav;
  })();

  const ranges = {
    d1: pct((latest.nav / prev.nav - 1) * 100),
    w1: byTradingDays(series, latest, 5),
    m1: byTradingDays(series, latest, 21),
    m3: byTradingDays(series, latest, 63),
    m6: byTradingDays(series, latest, 126),
    y1: byTradingDays(series, latest, 244),
    y3: byYears(series, latest, 3),
    y5: byYears(series, latest, 5),
    ytd: ytdBase ? pct((latest.nav / ytdBase - 1) * 100) : null,
    all: pct((latest.nav / first.nav - 1) * 100),
  };

  const recent = series.slice(-30).reverse().map(p => ({
    date: p.date,
    nav: p.nav,
    chg: p.chg == null ? (p === first ? null : pct((p.nav / series[series.indexOf(p) - 1]?.nav - 1) * 100)) : p.chg,
  }));

  const dd5y = maxDrawdown(win5y);
  const stats = {
    maxDrawdown: dd5y.pct,
    maxDrawdownFrom: dd5y.from,
    maxDrawdownTo: dd5y.to,
    volatility: volatility(win5y),
    upDays: pct((series.slice(-244).filter((p, i, arr) => i > 0 && p.nav > arr[i - 1].nav).length /
      Math.max(1, series.slice(-244).length - 1)) * 100, 1),
    bestDay: pct(Math.max(...series.slice(-244).map(p => p.chg ?? 0)), 2),
    worstDay: pct(Math.min(...series.slice(-244).map(p => p.chg ?? 0)), 2),
    from5yHigh: pct((latest.nav / win5yHigh.nav - 1) * 100),
    from5yLow: pct((latest.nav / win5yLow.nav - 1) * 100),
  };

  return {
    code,
    name,
    note: entry.note ?? null,
    rate: grabValue(src, 'fund_Rate'),
    minPurchase: grabValue(src, 'fund_minsg'),
    firstDate: first.date,
    latest: {
      date: latest.date,
      nav: latest.nav,
      accNav: accMap.get(latest.date) ?? null,
      chg: latest.chg ?? ranges.d1,
    },
    ranges,
    percentile: { y5: pct5y, y3: pct3y, all: pctAll, basisWindow: win5y.length > 250 ? '5y' : 'all' },
    stars: starsFromPercentile(starBasis),
    high5y: { nav: win5yHigh.nav, date: win5yHigh.date },
    low5y: { nav: win5yLow.nav, date: win5yLow.date },
    stats,
    yearly: yearlyReturns(series),
    dca: dcaBacktest(series, 100, 5),   // 每周 100 元，近 5 年
    recent,
    series5y: downsample(win5y.length > 250 ? win5y : series, 700).map(p => [p.date, p.nav]),
    totalPoints: series.length,
  };
}

/* ---------- 主流程 ---------- */
async function main() {
  const cfgPath = path.join(ROOT, 'funds.json');
  const fundsCfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
  const list = Array.isArray(fundsCfg) ? fundsCfg : fundsCfg.funds;
  if (!list || !list.length) throw new Error('funds.json 未配置任何基金');

  const results = [];
  for (const entry of list) {
    const code = String(entry.code ?? entry).trim();
    process.stdout.write(`抓取 ${code} … `);
    try {
      const f = await buildFund(entry);
      results.push(f);
      console.log(`✓ ${f.name} 最新 ${f.latest.date} ${f.latest.nav} 分位 ${f.percentile.y5}% ${f.stars}★`);
    } catch (e) {
      console.log(`✗ ${e.message}`);
      // 保留上一版该基金数据，避免一次抓取失败把榜单清空
      try {
        const prev = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/funds.json'), 'utf8'));
        const old = prev.funds?.find(x => x.code === code);
        if (old) { results.push(old); console.log(`   沿用上次数据（${old.latest?.date}）`); }
      } catch { /* 没有历史数据可沿用 */ }
    }
  }
  if (!results.length) throw new Error('所有基金抓取失败，未生成数据');

  const payload = {
    generatedAt: new Date().toISOString(),
    source: '天天基金（东方财富）pingzhongdata',
    starRule: '近5年净值分位：≤20% 5星，≤40% 4星，≤60% 3星，≤80% 2星，>80% 1星',
    funds: results.sort((a, b) => (b.stars ?? 0) - (a.stars ?? 0)),
  };

  fs.mkdirSync(path.join(ROOT, 'data'), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'data/funds.json'), JSON.stringify(payload, null, 2), 'utf8');
  fs.writeFileSync(
    path.join(ROOT, 'data/funds.js'),
    `/* 由 scripts/build-data.mjs 自动生成，请勿手改 */\nwindow.FUND_DATA = ${JSON.stringify(payload)};\n`,
    'utf8'
  );
  console.log(`\n完成：${results.length} 只基金 → data/funds.js (${(fs.statSync(path.join(ROOT, 'data/funds.js')).size / 1024).toFixed(0)} KB)`);
}

main().catch(e => { console.error(e.message); process.exit(1); });
