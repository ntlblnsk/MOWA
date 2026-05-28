test-pict-dist:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/mowa/MOWA/checkpoint' \
		--method 'mowa-test-pict-dist' \
		--test_path "/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/cut2center-256/" \
		"/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/cut2left-256/" \
		"/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/cut2right-256/" \
		"/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/resize-origin_aspekt/" \
		"/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/padding-256" \
		"/mnt/mowa/pictures/pictures-dist/wide_n_makro/resized512"

test-pict-rot:
	python test_origin.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/mnt/mowa/MOWA/checkpoint' \
		--method 'test-pict-rot' \
		--test_path "/mnt/mowa/pictures/pictures-rot/squared/" \
		"/mnt/mowa/pictures/pictures-rot/rectang"