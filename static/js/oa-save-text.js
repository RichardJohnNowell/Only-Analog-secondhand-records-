// oa-save-text-as-download
// start
function downloadFile(filename, content) {
    let element = document.createElement(a);
    // blob is a data type that can store binary data
    let blob = new Blob([content], { type: plain/text });
    // creates a DOM string containing a URL which
    // represents the object given in the parameter
    let fileUrl = URL.createObjectURL(blob);
    // sets the value of an attribute on the specified element
    element.setAttribute(href, fileUrl);
    element.setAttribute(download, filename);
    element.style.display = none;
    // method to move an element from one to another
    document.body.appendChild(element);
    element.click();
    // method removes a child from the DOM
    document.body.removeChild(element);
  }
  window.onload = () => {
    document.getElementById(download).
    addEventListener(click, e => {
      // value of the input box. have to use 'var'
      var filename = document.getElementById(filename).value;
      // value of the input in the text area
      let content = document.getElementById(oa_text).value;
      // The && operator indicates whether both operands are true.
      if (oa_filename && content) {
        downloadFile(filename, content);
      }
    }
  );};
  // end