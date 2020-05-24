function helpCard(){
  document.getElementById("overlay").style.display = "block";
  document.getElementById("help-card").style.display = "block";
}

function teamCard(){
  document.getElementById("overlay").style.display = "block";
  document.getElementById("team-card").style.display = "block";
}

function generateConfession(){

  if(document.getElementById("short").checked!=true && document.getElementById("medium").checked!=true && document.getElementById("long").checked!=true){
    alert("Please select a confession length!");
    return false;
  }

  document.getElementById("overlay").style.display = "block";
  document.getElementById("confession-card").style.display = "block";


  //setTimeout(function () {
  //      document.getElementById('loading').style.display='none';
  //  }, 5000);

  if(document.getElementById("short").checked==true){
    var shortData = {"content": ["Dear(bout God every night every year conversation Im looking up.", "Dearravereprotect attages in the sadeward timms pusok like no? Cinto them actually on chary interesting not constantly clla? Cpear is in an dagia sa pa.", "Deard-like a mention sna, mag since man jickown sa gapasasahan 'g bay. Crush.", "DearNdInd u theyeld I got liking it in my CSBAT graduates, 7yes back, koo Feer, there are going to them."]};

  	if(localStorage.getItem('scount') !== null)
  		var scount = localStorage.getItem('scount');
  	else
  		var scount = 0;
  	scount++;
    if(scount > 3)
      var scount = 0;
  	localStorage.setItem('scount', scount);
  	var scount = localStorage.getItem('scount');
    document.getElementById("confession").innerHTML = shortData.content[scount];
    console.log(shortData.content[scount]);
  }
  else if(document.getElementById("medium").checked==true){
    var medData = {"content": ["Dear!(like we wanted to hear or asian leader, they dont glash active. Checked minese joundly psych record suite of the servert and I don't make the daring stoa who can get to come on us.", "DearX,N8554. Hi Cans, I need you glad to my best friend. I just have come some straight acts.", "Dear+}VORNG EIEMTOY.\n\"Dana chikla. Thrre heart ."]}
  	if(localStorage.getItem('mcount') !== null)
  		var mcount = localStorage.getItem('mcount');
  	else
  		var mcount = 0;
  	mcount++;
    if(mcount > 3)
      var mcount = 0;
  	localStorage.setItem('mcount', mcount);
  	var mcount = localStorage.getItem('mcount');
    document.getElementById("confession").innerHTML = medData.content[mcount];
    console.log(medData.content[mcount]);

  }
  else if(document.getElementById("long").checked==true){
    var longData = { "content": ["Dear<_\\qWECADER,.\n(Ok/B/ETO, naa sila. Gi makit ko si ako batas siya sa [contrm. And the positive money evening misuberot A Cin my now..#7539: I'm super shrows about a Guster but I feel so gwapo but preted ki liight morrible, seeing away.", "DearBM!LZ+ NIGLENS, daphat pud nga crys ra mi pag tulod ko ug INgrema .\n\"\"Hi XUC.\nGod those addumt. Delice.\n\"Damer the street a part turty. Th*t.\"\" Katetay. Ako no year into. Human gyud sa akong jokegod jud karon ug kauwag-shirk sa iyang to sa parents. WAHO BARA! DO SU MANGION EV. Hog eve gasulod cya :).\nBut, di ko sa old from the Great day. I just give you so here does.", "Dearo'ver'here smart out of turns about with all the way and I was having some guys on your creditar names or how turned on SCM? I wasnt tublish, and respectment bare! As beat and wasnt to wear some night? The times\"#7879: \"Okay is called, not acroved but the on us have no names when they'd paid to a nymnt respect about this stories."] }
  	if(localStorage.getItem('lcount') !== null)
  		var lcount = localStorage.getItem('lcount');
  	else
  		var lcount = 0;
  	lcount++;
    if(lcount > 3)
      var lcount = 0;
  	localStorage.setItem('lcount', lcount);
  	var lcount = localStorage.getItem('lcount');
    document.getElementById("confession").innerHTML = longData.content[lcount];
    console.log(longData.content[lcount]);

  }

}

function switchOff(){
  document.getElementById("overlay").style.display = "none";
  document.getElementById("help-card").style.display = "none";
  document.getElementById("team-card").style.display = "none";
  document.getElementById("confession-card").style.display = "none";
}
