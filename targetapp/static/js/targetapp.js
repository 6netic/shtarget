
var formular = document.getElementById("myForm");

formular.addEventListener("submit", function(e) {
	e.preventDefault();
	document.getElementById("message").innerHTML = "";
	const p = document.createElement("p");
	var messResp = document.getElementById("message");
	var paragraph = messResp.appendChild(p);
	
	const file = document.getElementById("srcfile");
	const formData = new FormData(formular);
	formData.append("srcfile", file.files[0]);

	/* Ajax function */
	fetch("/", { method: "POST", body: formData })
	.then(function(response) {
			if(response.status == 500) {
				response.json().then(function(data) {
					paragraph.innerHTML = data.mess;
				});					
			}
			else if(response.status == 400) {
				response.json().then(function(data) {
					paragraph.innerHTML += data.mess;
				})
			}
			else if(response.status == 413) {
				response.json().then(function(data) {
					paragraph.innerHTML += data.mess;
				})
			}
			else if(response.status == 409) {
				response.json().then(function(data) {
					paragraph.innerHTML += data.mess;
				})
			}	
			else {
				response.json().then(function(data) {
					document.getElementById("formBlock").innerHTML = "";
					var output = document.getElementById("picture");
					var image = document.createElement("imageOutput");
					output.innerHTML = "<img src=static/out/temp.jpg?" + data + ">";
				})
			}	
	})
});














