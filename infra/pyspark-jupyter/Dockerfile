FROM jupyter/pyspark-notebook
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"
ENV JUPYTER_ENABLE_LAB=yes
RUN git clone https://github.com/luisbelloch/data_processing_course.git && \
    mv data_processing_course/data . && \
    mv data_processing_course/spark ./ejemplos && \
    rm -rf data_processing_course
