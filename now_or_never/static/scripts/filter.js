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
            self.all.addEventListener('change', () => {
                self.selectAll()
            })
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
//Live highlighting text
const $titles = document.querySelectorAll('.list_todo_title');
const $descriptions = document.querySelectorAll('.list_todo_description');
const $search = document.getElementById('search_fragment');

$search.addEventListener('input', (event) => {
    const searchText = event.target.value;
    const regex = new RegExp(searchText, 'gi');
    $titles.forEach(title => {
        textHighlight(title,regex)
    })
    $descriptions.forEach(description => {
        textHighlight(description,regex)
    })
});

function textHighlight(field,regex) {
    let text = field.innerHTML;
    text = text.replace(/(<mark class="highlight">|<\/mark>)/gim, '');
    field.innerHTML = text.replace(regex, '<mark class="highlight">$&</mark>');
}


//Date Range Picker Script
var start = moment().subtract(2, "days");
var end = moment();

function cb(start, end) {
    $("#kt_daterangepicker_4").html(start.format("MMMM D, YYYY") + " - " + end.format("MMMM D, YYYY"));
}

$("#kt_daterangepicker_4").daterangepicker({
    "locale": {
        "format": "DD/MM/YYYY",
        "separator": " - ",
        "applyLabel": "Apply",
        "cancelLabel": "Cancel",
        "fromLabel": "From",
        "toLabel": "To",
        "customRangeLabel": "Custom",
        "weekLabel": "W",
        "daysOfWeek": [
            "Su",
            "Mo",
            "Tu",
            "We",
            "Th",
            "Fr",
            "Sa"
        ],
        "monthNames": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ],
        "firstDay": 1
    },
    startDate: start,
    endDate: end,
    ranges: {
        "Today": [moment(), moment()],
        "Yesterday": [moment().subtract(1, "days"), moment().subtract(1, "days")],
        "Last 7 Days": [moment().subtract(6, "days"), moment()],
        "Last 30 Days": [moment().subtract(29, "days"), moment()],
        "This Month": [moment().startOf("month"), moment().endOf("month")],
        "Last Month": [moment().subtract(1, "month").startOf("month"), moment().subtract(1, "month").endOf("month")]
    }
}, cb);

cb(start, end);