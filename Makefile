test-wide_n_makro:
	python test.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/home/ubuntu/MOWA/checkpoint' \
		--method 'mowa-wide_n_makro' \
		--test_path "/home/ubuntu/pictures/pictures-dist/wide_n_makro/" \
		--task_id 1

test-ultrawide-cut2left-256:
	python test.py \
		--gpu 0 \
		--batch_size 1 \
		--model_path '/home/ubuntu/MOWA/checkpoint' \
		--method 'mowa-ultrawide-cut2left-256' \
		--test_path "/home/ubuntu/pictures/pictures-dist/ultrawide/preprocessing/cut2left-256/" \
		--task_id 1