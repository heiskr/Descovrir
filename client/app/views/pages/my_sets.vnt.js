const broker = require('../../modules/broker')
const tasks = require('../../modules/tasks')

module.exports = broker.add({
    'click .my-sets__engage-set': (e) => {
        if (e) { e.preventDefault() }
        const entityID = e.target.id
        tasks.chooseSet(entityID)
    }
})
