"use strict";
class Litter {
    x;
    y;
    vx;
    vy;
    constructor(x, y, vx, vy) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
    }
    //uus asukoht
    asukoht(sekundid) {
        let hetkeX = this.x;
        let hetkeY = this.y;
        let hetkeVx = this.vx;
        let hetkeVy = this.vy;
        for (let i = 0; i < sekundid; i++) {
            hetkeX += hetkeVx;
            hetkeY += hetkeVy;
            let v = Math.sqrt(hetkeVx * hetkeVx + hetkeVy * hetkeVy);
            if (v > 0) {
                let uusV = Math.max(0, v - 9);
                hetkeVx = (hetkeVx / v) * uusV;
                hetkeVy = (hetkeVy / v) * uusV;
            }
        }
        return { x: hetkeX, y: hetkeY, vx: hetkeVx, vy: hetkeVy };
    }
    kasOnPeatunud(aeg) {
        let olek = this.asukoht(aeg);
        return olek.vx === 0 && olek.vy === 0;
    }
}
/* function test(): void{
    const resultContainer = document.getElementById('results') as HTMLDivElement;
    const testLitter = new Litter(50, 50, 60, 40);
    const tulemus = testLitter.asukoht(10);

    if (tulemus.x === 20 && tulemus.y === 14){
        resultContainer.innerHTML = "Testarvutus on õige";
    } else{
        resultContainer.innerHTML = "Testarvutus on vale";
    }
} */
function draw() {
    const canvas = document.getElementById('litter');
    if (!canvas)
        return;
    const ctx = canvas.getContext('2d');
    if (!ctx)
        return;
    const litter = new Litter(50, 50, 60, 40);
    const sekundid = 10;
    for (let t = 0; t <= sekundid; t++) {
        const punkt = litter.asukoht(t);
        ctx.beginPath();
        ctx.arc(punkt.x, punkt.y, 5, 0, Math.PI * 2);
        ctx.fillStyle = (punkt.vx === 0 && punkt.vy === 0) ? "red" : "black";
        ctx.fill();
        ctx.fillText(`${t}s`, punkt.x + 8, punkt.y);
    }
}
window.onload = () => {
    //test();
    draw();
};
