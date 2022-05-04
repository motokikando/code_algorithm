
function main(input){
    const args = input.split("\n");
    const n = parseInt(args, 10);
    const l = [0]*(n+1);
    for(let i=2; i<n+1; i++ ){
        l[i] = l[i-2] + l[i-1]
    }
    return l[n];

}
main(require("fs").readFileSync("/dev/stdin", "utf8"));