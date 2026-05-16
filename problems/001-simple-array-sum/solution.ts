// Simple Array Sum
// https://www.hackerrank.com/challenges/simple-array-sum/problem

import * as readline from 'readline';

function simpleArraySum(ar: number[]): number {
    // Write your solution here
    return 0;
}

const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];

rl.on('line', (line: string) => lines.push(line.trim()));
rl.on('close', () => {
    const n = parseInt(lines[0]);
    const ar = lines[1].split(' ').map(Number);
    const result = simpleArraySum(ar);
    console.log(result);
});
