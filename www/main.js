$(document).ready(function () {
    eel.Start()();
    eel.expose(WishMessage)

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",

        },

        out: {
            effect: "bounceOut",
        }
    });

    $(".s-message").textillate({
        selector: '.s-message',
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },

        out: {
            effect: "fadeOutUp",
            sync: true,
        }
    });

    function WishMessage(message) {

        $(".text li:first").text(message);
        $('.text').textillate('start');

    }

    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {

        $("#Start").attr("hidden", true);
        eel.StartSound()();

        setTimeout(function () {
            $("#Oval").addClass("animate__animated animate__zoomIn");


        }, 1000)
        setTimeout(function () {
            $("#Oval").attr("hidden", false);


        }, 1000)
    }

    // When Click on BOB, it hide and display spectrum
    $("#MicBtn").click(function () {
        // $("#SpeakMessage").text("");
        $("#Oval").attr("hidden", true);

        $("#Spectrum").attr("hidden", false);
        eel.allCommands()();
    });




    // Python: Hide Spectrum after work

    eel.expose(hideSpectrum)
    function hideSpectrum() {
        $("#Oval").attr("hidden", false);
        $("#ChatDisplay").attr("hidden", false);
        $("#Spectrum").attr("hidden", true);
        $("#weather").attr("hidden", true);
        $(".s-message li:first").text("How can i help you");
        $('.s-message').textillate('start');
    }

    // open weather ui
    eel.expose(weatherShow)
    function weatherShow(state, weather, location, time) {
        $("#Spectrum").attr("hidden", true);
        $("#weather").attr("hidden", false);
        $("#state").text(state);
        $("#weather-num").text(weather);
        $("#location").text(location);
        $("#time").text(time);
    }

    eel.expose(SpeakMessage)
    function SpeakMessage(message) {
        // $(".s-message").text(message);
        $(".s-message li:first").text(message);
        $('.s-message').textillate('start');

    }


    // send and mic button change function

    $("#chatbox").keydown(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);

    });

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)

    });

    $("#chatbox").keypress(function (e) {
        if (e.key == "Enter") {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });


    /* ------------------------------------------------------------------------------------------
    Important Functions Start
    -------------------------------------------------------------------------------------------- */

    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#Spectrum").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }




    /* ------------------------------------------------------------------------------------------
    Important Functions Ends
    -------------------------------------------------------------------------------------------- */






























    //  Siri Wave Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: "0.30",
        amplitude: "1",
        autostart: true,
        // color: "#eb4034",
    });

    // document.getElementById("stopBtn").addEventListener("click", function () {
    //     siriWave.setAmplitude(0)
    //     // siriWave.start()

    //     setTimeout(function () {
    //         //your code to be executed after 1 second
    //         siriWave.stop()
    //         const element = document.getElementById('siri-container')
    //         element.classList.remove('animate__animated', 'animate__fadeIn');
    //         element.classList.add('animate__animated', 'animate__fadeOut');
    //     }, 500);
    // })
    // document.getElementById("startBtn").addEventListener("click", function () {
    //     const element = document.getElementById('siri-container')
    //     element.classList.remove('animate__animated', 'animate__fadeOut')
    //     element.classList.add('animate__animated', 'animate__fadeIn');
    //     siriWave.setAmplitude(0.9)
    //     siriWave.start()
    // })


    // window.oncontextmenu = function () {
    //     return false;
    // };

    document.addEventListener("keydown", function (event) {
        var key = event.key || event.keyCode;

        if (key == 123) {
            return false;
        } else if ((event.ctrlKey && event.shiftKey && key == 73) || (event.ctrlKey && event.shiftKey && key == 74)) {
            return false;
        }
    }, false);

});

