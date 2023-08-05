"use strict";

const { fishingRodNew, fishingRodLine, fishingRodCounter, fishingRodProgressBar } = require("./index.node");

// TODO: convert to Typescript
class Plotfish {
    constructor(apiKey, riverbedUrl = 'http://localhost:3000') {
        this.rod = fishingRodNew(riverbedUrl, apiKey);
    }

    line(plotName, value) {
        fishingRodLine.call(this.rod, plotName, value);
    }


    counter(plotName, change) {
        fishingRodCounter.call(this.rod, plotName, change);
    }


    progressBar(plotName, value, total) {
        fishingRodProgressBar.call(this.rod, plotName, value, total);
    }
}


module.exports = Plotfish;