var valueList = document.getElementById('valueList');
var text = '<span> You have orderded your burger with:</span>';
var listArray =[];

var checkboxes = document.querySelectorAll('.checkbox');

for (var checkbox of checkboxes) {
  checkbox.addEventListner('click', function() {
      if (this.checked == true) {
        listArray.push(this.value);
        valueList.innerHTML = text + listArray.join('/');
      } else {
        listArray = listArray.filter(e => e !== this.value);
        vlaueList.innerHTML = text + listArray.join('/');
      }
    })
  }

