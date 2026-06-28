.PHONY: starting

starting:
	rm -rf .venv && \
	export UV_CACHE_DIR=/mnt/data/MOWA/.uv-cache && \
	export UV_LINK_MODE=copy && \
	uv venv --python 3.8 && \
	source .venv/bin/activate && \
	uv pip install -r requirements.txt

test-dist:
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

test-dist-wide_n_makro256:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'mowa-test-pict-dist-wide_n_makro256' \
		--test_path "/mnt/data/pictures/pictures-dist/wide_n_makro/resized256"

test-rot:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-pict-rot' \
		--test_path "/mnt/data/pictures/pictures-rot/squared/" \
		"/mnt/data/pictures/pictures-rot/rectang"

test-fish:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'test-fish' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/all-resized256" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256" \
		"/mnt/data/pictures/pictures-fish/preproces-w_fr256" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/mine_newmask"

test-fish-max_frame:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'fish-max_frame' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/max_frame/CarparkA" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/max_frame/DriveC" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/max_frame/DriveE" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/max_frame/IMG"

test-fish-shrink_3:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'fish-shrink_3' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256/CarparkA" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256/DriveC" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256/DriveE" \
		"/mnt/data/pictures/pictures-fish/preprocessing/with-frame/all-256/IMG"

test-fish-big_size-mine:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/data/MOWA/checkpoint' \
		--method 'fish-big_size-mine' \
		--test_path "/mnt/data/pictures/pictures-fish/preprocessing/with-frame/big_size-mine"


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

