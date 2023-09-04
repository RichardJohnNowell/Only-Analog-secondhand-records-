// to download a text
// start
function elemTarget(e) {
	e = e || window.event;
	e.preventDefault();
	return e.target;
}
  document.addEventListener("click", function(e) {
	let elem = elemTarget(e);
  if (elem.id == 'buttonDownload') {
    saveText();
	}
});
// saving text
function saveText() {
	let data = document.querySelector('#texTareaI').value;
	let file = 'data-' + Date.now() + '.txt';
  let link = document.createElement('a');
	link.download = file;
  // raw data converted to text
	let blob = new Blob(['' + data + ''], {
		type: 'text/plain'
	});
	link.href = URL.createObjectURL(blob);
	link.click();
	URL.revokeObjectURL(link.href);
}
// end