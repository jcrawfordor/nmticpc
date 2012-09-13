var uTimer;
var dTimer;
var UpSeconds;
var DownSeconds;


function CreateTimer(uTimerID, uTime, dTimerID, dTime) {
        uTimer = document.getElementById(uTimerID);
        UpSeconds = uTime;
        dTimer = document.getElementById(dTimerID);        
        DownSeconds = dTime;

        UpdateTimer();
        window.setTimeout("Tick()", 1000);
}

function Tick() {
        DownSeconds -= 1;
        UpSeconds += 1;
        UpdateTimer();
        window.setTimeout("Tick()", 1000);
}

function UpdateTimer() {
        var Seconds = UpSeconds;
        
        var Days = Math.floor(Seconds / 86400);
        Seconds -= Days * 86400;

        var Hours = Math.floor(Seconds / 3600);
        Seconds -= Hours * (3600);

        var Minutes = Math.floor(Seconds / 60);
        Seconds -= Minutes * (60);


        var TimeStr = ((Days > 0) ? Days + " days " : "") + LeadingZero(Hours) + ":" + LeadingZero(Minutes) + ":" + LeadingZero(Seconds)


        uTimer.innerHTML = TimeStr;

        Seconds = DownSeconds;
        
        Days = Math.floor(Seconds / 86400);
        Seconds -= Days * 86400;

        Hours = Math.floor(Seconds / 3600);
        Seconds -= Hours * (3600);

        Minutes = Math.floor(Seconds / 60);
        Seconds -= Minutes * (60);


        TimeStr = ((Days > 0) ? Days + " days " : "") + LeadingZero(Hours) + ":" + LeadingZero(Minutes) + ":" + LeadingZero(Seconds)


        dTimer.innerHTML = TimeStr;

}


function LeadingZero(Time) {

        return (Time < 10) ? "0" + Time : + Time;

}

