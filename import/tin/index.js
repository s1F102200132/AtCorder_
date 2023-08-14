function tinderLike() {
    const min = 5, max = 10;
    const per = 100
    const rand_time = Math.floor(Math.random() * (max - min + 1) + min);
    const rand_flag = Math.floor(Math.random() * per);
    const good_elem = document.getElementsByClassName("button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a")[0];
    const bad_elem = document.getElementsByClassName("button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-nope):a")[0];
  
    try{
        if(rand_flag>30){
            good_elem.click();
        }else{
            bad_elem.click();
        }
    }catch(e){
      console.log( e.message );
    }
    setTimeout(tinderLike, rand_time * 1000);
  }
  
  
  tinderLike()

  