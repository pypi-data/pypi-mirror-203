(function(){
    let loc = window.location.pathname; // ===> /admin/elections/party/7/change/
    let arr = loc.split('/');
    let change_chunk_index = arr.indexOf('change');
    //console.log(arr, change_chunk_index);
    if(change_chunk_index == -1){
        return;
    }
    if(!(/\d+/.test(arr[change_chunk_index-1]))){
        return;
    }
    let prev_record_id = document.getElementById('prev_record_id').value || '';
    let next_record_id = document.getElementById('next_record_id').value || '';
    let data = {prev: prev_record_id, next: next_record_id};

    function add_np_link(npa_text, np_id){
        let record_path = loc.replace('/'+arr[change_chunk_index-1]+'/', '/'+np_id+'/')
        let npa = document.createElement('a');
        npa.setAttribute('href', record_path);
        npa.innerHTML = npa_text;
        document.querySelector('.prev_next').appendChild(npa);
    }
    if(data.prev){
        add_np_link('Previous', data.prev);
    }
    if(data.next){
        add_np_link('Next', data.next);
    }
})();