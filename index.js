export default {
  async fetch(request) {
    const url = new URL(request.url);
    url.hostname = "mzrf.github.io"; // 替换成你的 GitHub Pages 域名
    return fetch(url.toString(), request);
  }
}
