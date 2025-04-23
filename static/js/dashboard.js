const ctx = document.getElementById("tasksChart").getContext("2d");

const tasksChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: window.dashboardData.labels,
    datasets: [
      {
        label: "Completed Tasks",
        data: window.dashboardData.completedData,
        borderColor: "green",
        backgroundColor: "rgba(0, 128, 0, 0.2)",
        fill: true,
        tension: 0.3,
      },
      {
        label: "Terminated Tasks",
        data: window.dashboardData.terminatedData,
        borderColor: "red",
        backgroundColor: "rgba(255, 0, 0, 0.2)",
        fill: true,
        tension: 0.3,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 1,
        },
      },
    },
  },
});
