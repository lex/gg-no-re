riot.tag('enterprise-book-delete', '<table> <thead> <tr> <th>Title</th> <th>Author</th> <th>Pages</th> <th>Year</th> <th>Publisher</th> <th>Delete?</th> </tr> </thead> <tbody> <tr each="{ b in books }"> <td> { b.title } </td> <td> { b.author } </td> <td> { b.pages } </td> <td> { b.year } </td> <td> { b.publisher } </td> <td> <input type="checkbox" name="{ b.db_id }" id="{ b.db_id }" onclick="{ parent.handle_click }"> </td> </tr> </tbody> </table>', function(opts) {
        this.books = opts.books;
        this.add_id = opts.add_id;
        this.remove_id = opts.remove_id;

        this.handle_click = function(e) {
            var id = e.item.b.db_id;
            if (e.srcElement.checked)
                this.add_id(id);
            else
                this.remove_id(id);
            return true;
        }.bind(this);

    
});
