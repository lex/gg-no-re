riot.tag('inproceedings-edit', '<div class="row"> <div class="small-12 small-centered colums"> <p align="center"> <form method="post"> <input type="hidden" name="db_id" value="{ i.db_id }"> Author: <input type="text" name="author" value="{ i.author }" autofocus> <br> Title: <input type="text" name="title" value="{ i.title }"> <br> School: <input type="text" name="school" value="{ i.school }"> <br> Year: <input type="text" name="year" value="{ i.year }"> <br> <input type="submit" value="Apply changes" class="button"> </form> </p> </div> </div>', function(opts) {
        this.i = opts.i;
    
});
