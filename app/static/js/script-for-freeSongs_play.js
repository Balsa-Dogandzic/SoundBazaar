document.addEventListener("DOMContentLoaded", function() {
        var playButtons = document.querySelectorAll(".play-button");

        playButtons.forEach(function(button) {
            button.addEventListener("click", function() {
                var audioUrl = this.getAttribute("data-audio");
                var audio = new Audio(audioUrl);
                audio.play();
            });
        });
    });

