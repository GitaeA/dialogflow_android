package com.example.retrofit2test;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

interface APIInterface {

    @GET("api/text")
    Call<dialogflowData> doGetText();

    @GET("api/dialogflow?")
    Call<dialogflowData> doDialogflowText(@Query("question") String question);


}
