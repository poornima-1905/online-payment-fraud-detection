document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("file-input");
  const uploadBtn = document.getElementById("upload-btn");
  const analyzeBtn = document.getElementById("analyze-upload-btn");
  const uploadStatus = document.getElementById("upload-status");
  const resultsContainer = document.getElementById("results-table-container");
  const tableHead = document.querySelector("#results-table thead");
  const tableBody = document.querySelector("#results-table tbody");
  const riskChartCanvas = document.getElementById("riskChart");
  let currentFile = null;
  let riskChart = null;


  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      currentFile = fileInput.files[0];
      uploadStatus.classList.remove("hidden");
      uploadStatus.textContent = `File opened: ${currentFile.name}`;
      uploadStatus.classList.add("text-yellow-400");
    }
  });


  uploadBtn.addEventListener("click", () => {
    if (!currentFile) {
      uploadStatus.textContent = "No file selected.";
      uploadStatus.classList.remove("hidden");
      uploadStatus.classList.add("text-red-400");
      return;
    }

    uploadStatus.textContent = "Upload successful!";
    uploadStatus.classList.remove("text-yellow-400");
    uploadStatus.classList.add("text-green-400");

    setTimeout(() => {
      uploadStatus.classList.add("hidden");
    }, 5000);
  });

  analyzeBtn.addEventListener("click", async () => {
    if (!currentFile) return;

    const formData = new FormData();
    formData.append("file", currentFile);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze-upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (data.error) {
        alert("Error analyzing file.");
        return;
      }

      renderTable(data.columns, data.result);
      renderChart(data.risk_data);

      
      resultsContainer.scrollIntoView({ behavior: "smooth" });
    } catch (err) {
      alert("Server error. Please try again.");
    }
  });

  function renderTable(columns, rows) {
   
    tableHead.innerHTML = "";
    tableBody.innerHTML = "";

    
    const headerRow = document.createElement("tr");
    columns.forEach((col) => {
      const th = document.createElement("th");
      th.classList.add("py-2", "px-4");
      th.textContent = col;
      headerRow.appendChild(th);
    });
    tableHead.appendChild(headerRow);

  
    rows.forEach((row) => {
      const tr = document.createElement("tr");
      columns.forEach((col) => {
        const td = document.createElement("td");
        td.classList.add("py-2", "px-4");
        td.textContent = row[col];
        tr.appendChild(td);
      });
      tableBody.appendChild(tr);
    });
  }

  function renderChart(riskData) {
    const labels = riskData.map((d) => d.label);
    const counts = riskData.map((d) => d.count);

    if (riskChart) {
      riskChart.destroy();
    }

    riskChart = new Chart(riskChartCanvas, {
      type: "doughnut",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Risk Distribution",
            data: counts,
            backgroundColor: ["#ef4444", "#10b981"], // Red for Fraud, Green for Not Fraud
            borderColor: "#ffffff",
            borderWidth: 2
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom"
          }
        }
      }
    });
  }
});
