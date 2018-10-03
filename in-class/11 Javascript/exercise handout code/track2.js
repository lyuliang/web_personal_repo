var time = 0
var t

function reset() {
	time = 0
	document.getElementById('timeElapsed').innerHTML = time
}


function start() {
	document.getElementById('timeElapsed').innerHTML = time
	
	time += 1
	t = setTimeout("start()",1000)
}

function stop() {
	clearTimeout(t)
}


