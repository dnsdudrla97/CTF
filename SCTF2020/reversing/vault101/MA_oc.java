// True, False? s.a 함수에서 True 값을 가져와야 한다.
public void onClick(View view) {
    try {
        boolean a2 = this.s.a(this.p.getText().toString());
        Toast toast = new Toast(this);
        toast.setView(getLayoutInflater().inflate(a2 ? R.layout.toast_success_layout : R.layout.toast_fail_layout, (ViewGroup) findViewById(R.id.custom_toast_container)));
        toast.setGravity(17, 0, 0);
        toast.setDuration(1);
        toast.show();
        if (!a2) {
            this.p.getText().clear();
        }
    } catch (RemoteException e) {
        e.printStackTrace();
    }
}