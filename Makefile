test-pict-dist:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'mowa-test-pict-dist' \
		--test_path "/mnt/data/pictures/pictures-dist/ultrawide/preprocessing/cut2center-256/" \
		"/mnt/data/pictures/pictures-dist/ultrawide/preprocessing/cut2left-256/" \
		"/mnt/data/pictures/pictures-dist/ultrawide/preprocessing/cut2right-256/" \
		"/mnt/data/pictures/pictures-dist/ultrawide/preprocessing/resize-origin_aspekt/" \
		"/mnt/data/pictures/pictures-dist/ultrawide/preprocessing/padding-256" \
		"/mnt/data/pictures/pictures-dist/wide_n_makro/resized512"

test-pict-rot:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-pict-rot' \
		--test_path "/mnt/data/pictures/pictures-rot/squared/" \
		"/mnt/data/pictures/pictures-rot/rectang"

test-fish-wt-fr:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-fish-wt-fr' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/all-resized256"

test-fish-wt-fr2:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-fish-wt-fr2' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256"

test-fish-wt-fr_pozostale:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-fish-wt-fr' \
		--test_path "/mnt/data/pictures/pictures-fish/original/CarparkA" \
		"/mnt/data/pictures/pictures-fish/original/DriveC" \
		"/mnt/data/pictures/pictures-fish/original/DriveE" \
		"/mnt/data/pictures/pictures-fish/original/mine"

prepare_dataset_fish:
	python /mnt/data/MOWA/TESTprepare_dataset.py \
		/mnt/data/pictures/pictures-fish/preprocessing/all-resized256

prepare_dataset_fish2:
	python /mnt/data/MOWA/TESTprepare_dataset.py \
		/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256

resize_fish_wt_frame256:
	python /mnt/data/MOWA/TESTresize.py \
		--src "/mnt/data/pictures/pictures-fish/original/CarparkA" \
		--dst "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256" \
		--size 256 && \
	python /mnt/data/MOWA/TESTresize.py \
		--src "/mnt/data/pictures/pictures-fish/original/DriveC" \
		--dst "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256" \
		--size 256 && \
	python /mnt/data/MOWA/TESTresize.py \
		--src "/mnt/data/pictures/pictures-fish/original/DriveE" \
		--dst "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256" \
		--size 256 && \
	python /mnt/data/MOWA/TESTresize.py \
		--src "/mnt/data/pictures/pictures-fish/original/mine" \
		--dst "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256" \
		--size 256 \
    	--fix_orientation

