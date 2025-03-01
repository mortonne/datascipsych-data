load PolyEtal11_JEPLMC_data.mat

data.pres.category = data.pres_cat;
data.rec.category = data.rec_cat;

data.pres.period = zeros(size(data.pres_cat));
for i = 1:size(data.taskcatno, 1)
    for j = 1:size(data.taskcatno, 2)
        if ~isnan(data.taskcatno(i, j))
            cat = data.taskcatno(i, j);
            data.pres.period(i, data.pres_catnos(i, :) == cat) = j;
        end
    end
end
data.rec.period = data.rec_period;

data.pres.task = repmat(data.rec_task, 1, size(data.pres_items, 2));
data.rec.task = repmat(data.rec_task, 1, size(data.rec_items, 2));

tab = frdata2table(data, {'category', 'task', 'period'});
undef = cellfun(@(x) ~ischar(x) && isnan(x), tab.category);
tab.category(undef) = {'n/a'};

writetable(tab, '2011_Polyn.csv');
