let nn=24;
let tau = 2*Math.PI;
let matris = "{{1,1},{0,1}}";
for(var i =0;i<nn;i++) {
    let th = tau*i/nn;
    let x = (Math.cos(th)).toFixed(3);
    let y = (Math.sin(th)).toFixed(3); 
    console.log(`v${i}=Vector((${x},${y}))`);
    ggbApplet.evalCommand(`v${i}=Vector((${x},${y}))`);
    ggbApplet.evalCommand(`matrisA=${matris}`);
    ggbApplet.evalCommand(`w${i}=matrisA*v${i}`);
}

