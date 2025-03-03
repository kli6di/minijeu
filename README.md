
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini-Jeu des Portes</title>
    <style>
        /* Style CSS */
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #f9c5d1, #fce2e8);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            text-align: center;
            background-color: #fff;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 90%;
        }

        h1 {
            color: #ff6f61;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .portes {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }

        .porte {
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            background-color: #fff;
            border-radius: 15px;
            padding: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .porte:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .porte img {
            width: 150px;
            height: auto;
            border-radius: 10px;
        }

        #message {
            margin-top: 30px;
            font-size: 1.5em;
            color: #333;
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            animation: fadeIn 1s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Bouton pour rejouer */
        #rejouer {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 1em;
            color: #fff;
            background-color: #ff6f61;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        #rejouer:hover {
            background-color: #ff4a3d;
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
        <button id="rejouer" style="display: none;">Rejouer</button>
    </div>

    <script>
        // JavaScript
        const porteHeureuse = document.getElementById("porte-heureuse");
        const porteTriste = document.getElementById("porte-triste");
        const message = document.getElementById("message");
        const boutonRejouer = document.getElementById("rejouer");

        porteHeureuse.addEventListener("click", () => {
            message.textContent = "✨✨✨ Félicitations ! Tu es dans la salle heureuse ! ✨✨✨";
            message.style.color = "#4caf50";
            jouerSon("son_heureux.wav");
            afficherBoutonRejouer();
        });

        porteTriste.addEventListener("click", () => {
            message.textContent = "🌧️🌧️🌧️ Oh non... Tu es dans la salle triste... 🌧️🌧️🌧️";
            message.style.color = "#ff6f61";
            jouerSon("son_triste.wav");
            afficherBoutonRejouer();
        });

        function jouerSon(son) {
            const audio = new Audio(son);
            audio.play();
        }

        function afficherBoutonRejouer() {
            boutonRejouer.style.display = "block";
        }

        boutonRejouer.addEventListener("click", () => {
            message.textContent = "";
            boutonRejouer.style.display = "none";
        });
    </script>
</body>
</html>
