//Filter folders checkbox selection
class SelectionFilterFolders {
    constructor(filter_form) {
        this.folders = filter_form.querySelectorAll('input[name=folder]');
        this.all = filter_form.querySelector('input[name=all_folders]');
    }

    initialize() {
        const self = this
        if (self.folders && self.all) {
            self.folders.forEach(folder => {
                folder.addEventListener('change', function () {
                    if (self.isAllSelected(self.folders)) {
                        self.selectAll()
                    } else {
                        self.all.checked = false
                    }
                })
            })
            self.all.addEventListener('change', ()=>{self.selectAll()})
        }
    }

    selectAll() {
        this.folders.forEach(input => {
            input.checked = false;
        })
        this.all.checked = true
    }

    isAllSelected(folder_set) {
        let arr = [];
        for (let i = 0; i < folder_set.length; i++) {
            arr[i] = folder_set[i].checked
        }
        return arr.every(element => element === true)
    }
}


let filter_form = document.querySelector('#filter_form')
if (filter_form) {
    const filterForm_foldersControl = new SelectionFilterFolders(filter_form)
    filterForm_foldersControl.initialize()
}
