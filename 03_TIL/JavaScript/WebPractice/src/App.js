import Table from "./Table.js";
class App {
  // __init__ 같은 존재
  constructor($app) {
    this.$app = $app;
    this.render();
  }
  async render() {
    try {
      const response = await fetch("./src/data.json");
      if (response.ok) {

        new Table(data);
      }
    } catch {}
  }
}
export default App;
