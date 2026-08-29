// Season Bar Chart
const ctx = document.getElementById('seasonChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: seasons,
        datasets: [{
            label: 'Matches Played',
            data: season_matches,
            backgroundColor: "#4FC3F7",
            borderColor: "#03A9F4",
            borderWidth: 2,
            borderRadius: 8
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Winning Teams Pie Chart
const ctx2 = document.getElementById('winnerChart');

new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: winning_teams,
        datasets: [{
            data: winning_counts,
            backgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56",
                "#4BC0C0",
                "#9966FF",
                "#FF9F40",
                "#8BC34A",
                "#E91E63",
                "#03A9F4",
                "#9C27B0"
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Winning Teams Doughnut Chart
const ctx3 = document.getElementById('topWinningChart');

new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: winning_teams,
        datasets: [{
            data: winning_counts,
            backgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56",
                "#4BC0C0",
                "#9966FF",
                "#FF9F40",
                "#8BC34A",
                "#E91E63",
                "#03A9F4",
                "#9C27B0"
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Player of the Match Chart
const ctx4 = document.getElementById('playerChart');

new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: top_players,
        datasets: [{
            label: 'Player of the Match Awards',
            data: top_awards,
            backgroundColor: "#FF9800",
            borderColor: "#F57C00",
            borderWidth: 2,
            borderRadius: 8
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
               ticks: {
                   maxRotation:45,
                   minRotation:45
                }
            },
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx5 = document.getElementById('venueChart');

new Chart(ctx5, {
    type: 'bar',
    data: {
        labels: top_venues,
        datasets: [{
            label: 'Matches',
            data: venue_matches,
            backgroundColor: "#4FC3F7",
            borderColor: "#03A9F4",
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
new Chart(document.getElementById("batsmanChart"), {
    type: "bar",
    data: {
        labels: batsman_names,
        datasets: [{
            label: "Runs",
            data: batsman_runs
        }]
    }
});