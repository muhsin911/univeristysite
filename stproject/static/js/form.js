let pstate = document.querySelector("#pstate")
    let pcity = document.querySelector("#pcity")
    let pzip = document.querySelector("#pzip")
    let pphonenumber = document.querySelector("#pphonenumber")

    let tstate = document.querySelector("#tstate")
    let tcity = document.querySelector("#tcity")
    let tzip = document.querySelector("#tzip")
    let tphonenumber = document.querySelector("#tphonenumber")

    let sameaspermanent = document.querySelector("#sameaspermanent")
    sameaspermanent.addEventListener('change', () => {
            if (sameaspermanent.checked === true) {
                tstate.value = pstate.value;
                tcity.value = pcity.value;
                tzip.value = pzip.value;
                tphonenumber.value = pphonenumber.value;
            } else if (sameaspermanent.checked === false) {
                tstate.value = "";
                tcity.value = "";
                tzip.value = "";
                tphonenumber.value = "";
            }
        })


