let running = false;
let timerInterval = null;

function beep() {
    alert("Beep!"); // Cambiar por un sonido real si es necesario
}

function startTimer() {
    if (running) return;

    let minutes = parseInt(document.getElementById("minutes").value) || 0;
    let seconds = parseInt(document.getElementById("seconds").value) || 0;
    let totalTime = minutes * 60 + seconds;

    if (seconds < 0 || seconds >= 60 || totalTime <= 0) {
        alert("Por favor, introduce un valor válido para los minutos y segundos (segundos de 0 a 59).");
        return;
    }

    running = true;
    timerInterval = setInterval(() => {
        if (totalTime <= 0) {
            clearInterval(timerInterval);
            document.getElementById("timer").textContent = "00:00";
            beep(); // Reproducir beep 3 veces
            running = false;
            return;
        }

        totalTime--;
        let mins = Math.floor(totalTime / 60);
        let secs = totalTime % 60;
        document.getElementById("timer").textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
    document.getElementById("timer").textContent = "00:00";
    running = false;
}
