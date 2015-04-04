riot.tag('enterprise-book-list', '<table if = { this.books.length > 0 }> <thead> <tr> <th>Title</th> <th>Author</th> <th>Pages</th> <th>Year</th> <th>Publisher</th> </tr> </thead> <tbody> <tr each="{ b in this.books }"> <td> { b.title } </td> <td> { b.author } </td> <td> { b.pages } </td> <td> { b.year } </td> <td> { b.publisher } </td> <td> <a href="edit_book/{ b.db_id }">edit</a> </td> </tr> </tbody> </table> <style>', function(opts) {
        this.books = opts.books;
        this.edit_callback = opts.edit_callback;

        this.edit_this = function(e) {
            var id = e.item.b.db_id;
            this.edit_callback(id);
        }.bind(this);
    
});
