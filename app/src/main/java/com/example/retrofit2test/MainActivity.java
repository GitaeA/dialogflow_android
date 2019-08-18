package com.example.retrofit2test;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    TextView responseText;
    APIInterface apiInterface;
    Button sendButton;
    EditText requestText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        responseText = findViewById(R.id.responseText);
        requestText = findViewById(R.id.requestText);
        sendButton = findViewById(R.id.shoot);

        apiInterface = APIClient.getClient().create(APIInterface.class);


        sendButton.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {

                Call<dialogflowData> call = apiInterface.doDialogflowText(requestText.getText().toString());
                call.enqueue(new Callback<dialogflowData>() {

                    @Override
                    public void onResponse(Call<dialogflowData> call, Response<dialogflowData> response) {

                        Log.d("TAG", response.code()+"");

                        String displayResponse = "";

                        dialogflowData resource = response.body();
                        String text = resource.text;

                        responseText.setText(text);
                    }
                    @Override
                    public void onFailure(Call<dialogflowData> call, Throwable t) {
                        Log.d("TAG", t.toString());
                        call.cancel();
                    }
                });

            }
        });

//
//
//        Call<dialogflowData> call = apiInterface.doDialogflowText("음식");
//        call.enqueue(new Callback<dialogflowData>() {
//
//            @Override
//            public void onResponse(Call<dialogflowData> call, Response<dialogflowData> response) {
//
//                Log.d("TAG", response.code()+"");
//
//                String displayResponse = "";
//
//                dialogflowData resource = response.body();
//                String text = resource.text;
//
//                responseText.setText(text);
//            }
//            @Override
//            public void onFailure(Call<dialogflowData> call, Throwable t) {
//                Log.d("TAG", t.toString());
//                call.cancel();
//            }
//        });


    }


}
