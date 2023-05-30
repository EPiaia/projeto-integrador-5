//Dialog
function openDialog(dialogId) {
    var dialog = document.getElementById(dialogId);
    dialog.showModal();
  }
  
  function closeDialog(dialogId) {
    var dialog = document.getElementById(dialogId);
    dialog.close();
}

//Dropdown
$(document).ready(function () {
    $('#animal-search').select2({
      placeholder: 'Animal',
      allowClear: true,
    });
  });
  
  $(document).ready(function () {
    $('#pessoa-search').select2({
      placeholder: 'Pessoa',
      allowClear: true,
    });
  });

//Image picker
const fileInput = document.getElementById('file-input');
const imageList = document.querySelector('.image-list');

fileInput.addEventListener('change', function(event) {
  const files = Array.from(event.target.files);
  files.forEach(function(file) {
    const listItem = document.createElement('li');
    listItem.textContent = file.name;

    const removeIcon = document.createElement('i');
    removeIcon.className = 'fas fa-times remove-icon';
    removeIcon.addEventListener('click', function() {
      listItem.remove();
    });

    listItem.appendChild(removeIcon);
    imageList.appendChild(listItem);
  });
});

//toggle
function toggleRow(rowId) {
    var row = document.getElementById(rowId);
    row.classList.toggle('visible');
}