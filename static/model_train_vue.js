$(document).ready(function () {
    var index = 0;
    //$('#output').append(var_name + " = []" + '\n\n');

    function load_training_data(results, index, entities) {
        // get tokenized data
        var data = results[index];

        // clear dom
        $('#tokens').html("");

        // put number trained in header
        $('.trained').text("Trained: " + index + " / " + results.length);

        // add entity chooser
        $('.entity_choose').html('');
        generate_checkboxes(entities, $('.entity_choose'));

        // add options to dom
        for (var i = 0, l = data.length; i < l; i++) {
            var v = data[i];
            var li = $('<span class="token"></token>');
            li.text(v);
            li.attr('data-index', i);
            li.attr('data-token', v);
            console.log(li);
            $('#tokens').append(li);
        }

        $('.token').click(function () {
            if ($(this).attr('data-entity') !== undefined) {
                $(this).removeAttr('data-entity');
            } else {
                $(this).attr('data-entity', $('input[name="entities"]').val());
            }
        });


        // set initial code for output
        //variable = var_name;
        //var train_instance = variable + '.append(ner_training_instance(' + JSON.stringify(data) + '))';
        //$('#output').append(train_instance + '\n\n')
    }

    function generate_checkboxes(entities, checks) {
        for (var j = 0, e = entities.length; j < e; j++) {
            if (j === 0) {
            checks.append($('<label><input type="radio" name="entities" value="'+ entities[j] +'" checked>'+ entities[j] +'</label>'));
            } else {
            checks.append($('<label><input type="radio" name="entities" value="'+ entities[j] +'">'+ entities[j] +'</label>'));
            }
        }
    }

    function generate_training_code() {
        var entities = {};
        
        // get checked boxes and put into object
        $('.token').each(function (i, v) {
            if ($(v).attr('data-entity') !== undefined) {
                ent = $(v).attr('data-entity');
                if (entities[ent] !== undefined) {
                    entities[ent].push(i);
                } else {
                    entities[ent] = [i];
                }
            }
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
                code = variable + "[" + index + "]" + ".add_entity(xrange(" + firstIndex + "," + lastIndex + "), \"" + entity + "\")";
                code += " # ";
                for (var x = firstIndex; x < lastIndex; x++) {
                    code += $('.token[data-index="' + x + '"]').attr('data-token') + " ";
                }
                $('#output').append(code+ '\n')
            }
        });
        $('#output').append('\n')
    }

    //load_training_data(input_data, index, entities);

    //$('#generate_code').click(function () {
        //generate_training_code();
        //$("html, body").animate({ scrollTop: 0  }, "fast");
        //if (index < input_data.length - 1) {
            //index++;
            //load_training_data(input_data, index, entities);
        //} else {
            //alert("Done tagging models!");
            //index++;
            //$('.trained').text("Trained: " + index + " / " + entities.length);
            //$('#tokens').html("");
        //}
    //});
});

