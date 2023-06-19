function checkboxClicked(checkbox) {
    var checkboxes = document.getElementsByName("jabatan");
    for (var i = 0; i < checkboxes.length; i++) {
      checkboxes[i].checked = false;
    }
    checkbox.checked = true;
  }