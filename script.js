const fs = require('fs');
const path = require('path');

const directoryPath = ''

fs.readdir(directoryPath, (err, files) => {
    if (err) {
        return console.log('Erro ao listar arquivos: ' + err);
    } 
    files.forEach(file => {
        console.log(file);
    });
});