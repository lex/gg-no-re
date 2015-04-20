<book-edit>
    <div class='row'>
        <div class='small-12 small-centered colums'>
            <p align='center'>
                <form method='post'>
                    <input type='hidden' name='db_id' value={ book.db_id }>
                    Title:
                    <input type='text' name='title' value={ book.title } autofocus>
                    <br>
                    Author:
                    <input type='text' name='author' value={ book.author }>
                    <br>
                    Pages:
                    <input type='text' name='pages' value={ book.pages }>
                    <br>
                    Year:
                    <input type='text' name='year' value={ book.year }>
                    <br>
                    Publisher:
                    <input type='text' name='publisher' value={ book.publisher }>
                    <br>
                    Reference:
                    <input type='text' name='reference' value={ book.reference }>
                    <br>
                    <input type='submit' value='Apply changes' class='button'>
                </form>
            </p>
        </div>
    </div>
    <script>
        this.book = opts.book;
    </script>
</book-edit>
