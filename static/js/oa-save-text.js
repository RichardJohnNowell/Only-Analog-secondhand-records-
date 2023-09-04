// -------------------------- LEVEL I ---------------

lIDownload.onclick = (function(){
  doDL(document.getElementById("myTextArea").value);
  });
  
  function doDL(s){
      function dataUrl(data) {return "data:x-application/text," + escape(data);}
      window.open(dataUrl(s));
  }
  
  // -------------------------- LEVEL II ---------------
  
  const stack = {
   some: "stuffs",
   alot: "of them!"
  }
  
  jsonDownload.onclick = (function(){
    let j = document.createElement("a");
    j.download = "stack_" + Date.now() + ".json";
    j.href = URL.createObjectURL(new Blob([JSON.stringify(stack, null, 2)]));
    j.click()
  });
  
  // -------------------------- LEVEL III ---------------
  
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
  
  function saveText() {
    let data = document.querySelector('#texTareaI').value;
    let file = 'data-' + Date.now() + '.txt';
  
    let link = document.createElement('a');
    link.download = file;
    let blob = new Blob(['' + data + ''], {
      type: 'text/plain'
    });
    link.href = URL.createObjectURL(blob);
    link.click();
    URL.revokeObjectURL(link.href);
  }
  