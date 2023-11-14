const parentheticalPossibilities = (s) => {
    if (s.indexOf(`(`) === -1) return [s];
    let strWithOutFirst = s.slice(1);
    let options = s.charAt(0) === `(` ? [] : [s.slice(0, 1)];
    if (s.charAt(0) === `(`) {
        let i = 1;
        while (s.charAt(i) !== `)`) {
            options.push(s.charAt(i));
            i++;
        }

        strWithOutFirst = s.slice(i + 1);
    }

    subsWithoutFirst = parentheticalPossibilities(strWithOutFirst);
    let result = [];
    options.forEach(sub => {
        let subs = subsWithoutFirst.map(str => sub + str);

        result = result.concat(subs);
    })
    return result;
};

console.log(parentheticalPossibilities("(qr)ab(stu)c"));