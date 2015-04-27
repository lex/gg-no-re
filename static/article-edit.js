riot.tag('article-edit', '<div class="row"> <div class="small-12 small-centered colums"> <p align="center"> <form method="post"> <input type="hidden" name="db_id" value="{ article.db_id }"> Author: <input type="text" name="author" value="{ article.author }" autofocus> <br> Title: <input type="text" name="title" value="{ article.title }"> <br> Journal: <input type="text" name="journal" value="{ article.journal }"> <br> Year: <input type="text" name="year" value="{ article.year }"> <br> Volume: <input type="text" name="volume" value="{ article.volume }"> <br> Reference: <input type="text" name="reference" value="{ article.reference }"> <br> <input type="submit" value="Apply changes" class="button"> </form> </p> </div> </div>', function(opts) {
        this.article = opts.article;
    
});
