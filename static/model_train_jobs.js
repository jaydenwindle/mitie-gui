$(document).ready(function () {
    var index = 0;
    var var_name = "sample"
    var entities = [
        'language',
        'concept',
        'tool',
        'discipline'
    ]

    function load_training_data(results, index, entities) {
        // get tokenized data
        var data = results[index]['description_tokenized'];

        // clear dom
        $('.list-group').html("");

        //// put number trained in header
        //$('.trained').text("Trained: " + index + " / " + results.length);

        // add options to dom
        for (var i = 0, l = data.length; i < l; i++) {
            var v = data[i];
            var li = $('<li class="list-group-item"></li>');
            var sel = generate_checkboxes(entities);
            li.text(v);
            li.attr('data-index', i);
            li.attr('data-token', v);
            li.append(sel);
            console.log(li);
            $('.list-group').append(li);
        }

        variable = var_name + "[" + index.toString() + "]";
        
        $('#output').append("# Data: " + results[index]['jobtitle'] + " @ " + results[index]['company'] + '\n')
        $('#output').append("# URL: " + results[index]['url'] + '\n')
        var code = variable + ' = ner_training_instance(' + JSON.stringify(data) + ')';
        $('#output').append(code + '\n\n')
    }

    function generate_checkboxes(entities) {
        var checks = $('<span></span>')
        checks.css('float', 'right')
        for (var j = 0, e = entities.length; j < e; j++) {
            checks.append($('<label><input type="checkbox" name="'+ entities[j] +'" value="'+ entities[j] +'">'+ entities[j] +'</label>'));
        }
        return checks;
    }

    function generate_training_code() {
        var entities = {};
        
        // get checked boxes and put into object
        $('.list-group li').each(function (i, v) {
            $(v).find('input:checked').each(function (index, input) {
                if (entities[$(input).val()] != undefined) {
                    entities[$(input).val()].push(i);
                } else {
                    entities[$(input).val()] = [i];
                }
            });
        });

        // loop through results and turn indexes to code
        $.each(entities, function (entity, indexes) {
            for (var i = 0, l = indexes.length; i < l; i++) {
                var firstIndex = indexes[i];
                var lastIndex = firstIndex + 1;
                while (indexes[i + 1] == indexes[i] + 1) {
                    i++;
                }
                if (indexes[i] != firstIndex) {
                    // multiple tags in a row
                    lastIndex = indexes[i] + 1;
                }
                code = variable + ".add_entity(xrange(" + firstIndex + "," + lastIndex + "), \"" + entity + "\")";
                code += " # ";
                for (var x = firstIndex; x < lastIndex; x++) {
                    code += $('li.list-group-item[data-index="' + x + '"]').attr('data-token') + " ";
                }
                console.log(code);
                $('#output').append(code+ '\n')
            }
        });
        $('#output').append('\n')

        console.log(results);
    }


    //$('#generate_code').click(function () {
        //generate_training_code();
        //$("html, body").animate({ scrollTop: 0  }, "fast");
        //index++;
        //load_training_data(results, index, entities);
    //});

    $('#output').append("# Dataset: " + dataset_name + '\n\n')
    //load_training_data(results, index, entities);

});

