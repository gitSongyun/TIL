class Table {
  constructor(data) {
    this.data = data;
    console.log(data)
    this.render();
    displayTableHead = () => {
      const thead = document.createElement("thead");
      const theadTr = document.createElement("tr");
      for (let i = 0; i < 4; i++) {
        const th = document.createElement("th");
        th.appendChild(document.createTextNode());
        theadTr.appendChild(th);
      }
      thead.appendChild(theadTr);
      return thead;
    };
  }
  render() {
    const table = document.createElement("table");
    
    const thead = this.displayTableHead();
    table.appendChild(thead);
    
    document.getElementById("table").appendChild(table);
  }
}
export default Table;
