function Input_Check(){
  var flag = true;

  alert("hello, flask.")
  
  if (input_form.name.value == ""){
    alert("『名前』を入力してください");
    flag = false;
  };
  
  if (input_form.age.value == ""){
    alert("『年齢』を入力してください");
    flag = false;
  };
  
  if (input_form.sex.value == ""){
    alert("『性別』を入力してください");
    flag = false;
  };
  
  return flag;
}