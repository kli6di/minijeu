html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini-Jeu des Portes</title>
    <style>
        /* Style CSS */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            text-align: center;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
        }

        .portes {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }

        .porte {
            cursor: pointer;
            transition: transform 0.2s;
        }

        .porte:hover {
            transform: scale(1.1);
        }

        .porte img {
            width: 200px;
            height: auto;
            border-radius: 10px;
        }

        #message {
            margin-top: 20px;
            font-size: 1.2em;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Choisis une porte !</h1>
        <div class="portes">
            <div class="porte" id="porte-heureuse">
                <img src="porte_heureuse.jpg" alt="Porte Heureuse">
            </div>
            <div class="porte" id="porte-triste">
                <img src="porte_triste.jpg" alt="Porte Triste">
            </div>
        </div>
        <p id="message"></p>
    </div>

    <script>
        // JavaScript
        const porteHeureuse = document.getElementById("porte-heureuse");
        const porteTriste = document.getElementById("porte-triste");
        const message = document.getElementById("message");

        porteHeureuse.addEventListener("click", () => {
            message.textContent = "✨✨✨ Félicitations ! Tu es dans la salle heureuse ! ✨✨✨";
            message.style.color = "green";
            jouerSon("son_heureux.wav"); // Joue un son heureux
        });

        porteTriste.addEventListener("click", () => {
            message.textContent = "🌧️🌧️🌧️ Oh non... Tu es dans la salle triste... 🌧️🌧️🌧️";
            message.style.color = "red";
            jouerSon("son_triste.wav"); // Joue un son triste
        });

        function jouerSon(son) {
            const audio = new Audio(son);
            audio.play();
        }
    </script>
</body>
</html>
