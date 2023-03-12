//hide-display checkboxes

const checkboxes = Array.from(document.querySelectorAll('.mytable input[type="checkbox"]'));
const selectColBtn = document.getElementById("select_columns")
let f1=1 //flag

selectColBtn.addEventListener("click",
    (ele)=>{
        if(f1){
            checkboxes.forEach((checkbox, index) => {
                checkbox.classList.remove("deactive")
                checkbox.classList.add("active")
              });
              f1=0
        }else{
            checkboxes.forEach((checkbox, index) => {
                checkbox.classList.remove("active")
                checkbox.classList.add("deactive")
              });
              f1=1
        }

    }
)