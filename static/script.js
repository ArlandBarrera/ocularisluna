function fetchMoonPhases() {
  let startDate = document.getElementById("start").value;
  let endDate = document.getElementById("end").value;

  if (!startDate || !endDate) {
    alert("Por favor, seleccione ambas fechas.");
    return;
  }

  fetch(`/get_moon_phases?start_date=${startDate}&end_date=${endDate}`)
    .then((response) => response.json())
    .then((data) => {
      let resultList = document.getElementById("results");
      resultList.innerHTML = "";

      if (data.error) {
        resultList.innerHTML = `<li style="color:red">${data.error}</li>`;
        return;
      }

      data.phases.forEach((item) => {
        let li = document.createElement("li");
        li.textContent = `${item.date} - ${item.phase}`;
        resultList.appendChild(li);
      });

      document.getElementById("moonPlot").src = data.plot;
    })
    .catch((error) => console.error("Error:", error));
}
