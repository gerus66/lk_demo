
function delete_confirm (id1, id2){
 if confirm('Вы уверены, что хотите отменить регистрацию?')
  document.location.href = "/admin/lk/userregister/" + str(id1) + "/" + str(id2) + /reverse";
 else
    document.location.href = "/admin/lk/questionsform";
 }
 
function collapse_theme (theme){
 var c = document.getElementById(theme)
 alert (theme)
 var cl = c.className
 if (cl = ""){
     cl = "theme-off"
 }
 else {
     cl = ""
 }
 
}
