riot.tag('reference-manager', '<div class="row" if="{ opts.books.length > 0 }"> <div class="small-12 small-centered columns"> <p align="center"> <enterprise-book-list books="{opts.books}"> </p> </div> </div> <div class="row"> <div class="small-12 small-centered columns"> <p align="center"><a href="add_book" class="button">Add a new book</a></p> </div> </div>', function(opts) {

});

riot.tag('enterprise-book-list', '<table> <thead> <tr> <th each="{ th in tableheads }">{ th }</th> </tr> </thead> <tbody> <tr each="{ b in books }"> <td style="max-width: 250px; word-wrap: break-word"> { b.title } </td> <td style="max-width: 250px; word-wrap: break-word"> { b.author } </td> <td style="max-width: 250px; word-wrap: break-word"> { b.pages } </td> <td style="max-width: 250px; word-wrap: break-word"> { b.year } </td> <td style="max-width: 250px; word-wrap: break-word"> { b.publisher } </td> <td> <a href="edit_book/{ b.db_id }">edit</a> </td> <td> <a href="delete_book/{ b.db_id }">delete</a> </td> </tr> </tbody> </table>', function(opts) {
        this.books = opts.books;
        this.edit_callback = opts.edit_callback;
        this.tableheads = ['Title', 'Author', 'Pages', 'Year', 'Publisher'];
    
});
